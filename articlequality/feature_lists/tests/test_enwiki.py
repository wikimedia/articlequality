from revscoring.datasources.revision_oriented import revision
from revscoring.dependencies import solve

from .. import enwiki

revision_text = revision.text


def test_cite_templates():
    text = """
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text. {{foo}} {{{cite}}}  {{sfn}}  {{Harvard citation}}

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    assert solve(enwiki.all_ref_tags, cache={revision_text: text}) == 3
    assert solve(enwiki.all_cite_templates, cache={revision_text: text}) == 5


def test_infobox_templates():
    text = """
    {{Infobox pants|hats=2|pajams=23}}
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text.

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    assert solve(enwiki.infobox_templates, cache={revision_text: text}) == 1


def test_cn_templates():
    text = """
    {{Infobox pants|hats=2|pajams=23}}
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    I am a new paragraph.{{fact|date=never}}

    I am a new paragraph.{{Citation_needed|date=never}}
    """
    assert solve(enwiki.cn_templates, cache={revision_text: text}) == 3


def test_who_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    I am a new paragraph.{{who}}

    I am a new paragraph.{{who|date=today}}
    """
    assert solve(enwiki.who_templates, cache={revision_text: text}) == 2


def test_main_article_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    == Some section ==
    {{Main|section}}

    I am a new paragraph.{{who|date=today}}
    """
    assert solve(enwiki.main_article_templates,
                 cache={revision_text: text}) == 1


def test_paragraphs_without_refs_total_length():
    text = """
    Here is the first paragraph.
    It contains some references <ref>first reference</ref>.

    Here is second paragraph. One line with reference <ref>reference</ref>.

    Here is third paragraph.
    It has two lines, but no references.


    Here is fourth paragraph.
    It has two lines <ref>reference</ref>.
    One of which has a reference.

    Here is fifth paragraph. One line, no references.

    Short line.<ref>last</ref><ref>One more reference</ref>
    """
    assert solve(enwiki.paragraphs_without_refs_total_length,
                 cache={revision_text: text}) == 114


def test_image_links():
    text = """
            [[File:image.jpg|options|caption]]
            [[File:sound.ogg|options|a sound]]
            [[File:display.svg|options|caption]]
            """
    assert solve(enwiki.image_links, cache={revision_text: text}) == 3


def test_image_templates():
    text = """
            {{wide image|Helsinki z00.jpg|400px|
            |alt=Panorama of city with mixture of story buildings}}

            {{Panorama
            |image   = File:Ushuaia_panorama_from_seaside_big.jpg}}

            {{tall image|Polarisation_(Circular).svg}}

            {{scalable image|Dew on grass Luc Viatour.jpg}}

            {{Panorama 2
            | Image = image file name (don't need Files:)}}
            """
    assert solve(enwiki.image_templates, cache={revision_text: text}) == 5


def test_image_in_tags():
    text = """
            <gallery widths="125px" heights="154px">
            File:Alexander Andrejewitsch Iwanow 003.jpg|Study of head of John
            File:Ivanov Head4 gtg 17647.jpg|Ivanov head of Christ
            </gallery>
            <imagemap>
            Image:PolierMartinWombwellZoffany.jpg|thumb|200px|Colonel Antoine
            Polier
            rect 269 140 344 305 [[Claude Martin]]
            rect 124 147 181 298 [[Antoine Polier|Antoine-Louis Polier]]
            desc none
            </imagemap>
            """
    assert solve(enwiki.images_in_tags, cache={revision_text: text}) == 3


def test_image_in_templates():
    text = """
            {{multiple image
             | align = left
             | image1 = Frecklesmule.jpg
             | width1 = 143
             | alt1 = A mule
             | link1 = Mule
             | caption1 = A mule<br />(骡子 ''luózi'')}}
            {{Image array
            | perrow = 2
            | width = 140
            | height = 140
            | border-width = 2
            | image1 = On The Streets of Vilnius (5984257911).jpg
            | alt1 = alt1 | text1 = text1 | link1 = Vilnius}}
            {{Gallery
            |title=Cultural depictions of George Washington
            |width=160 | height=170
            |align=center
            |footer=Example 1
            |File:Federal Hall NYC 27.JPG
            |alt1=Statue facing a city building with Greek columns
            and huge U.S. flag
            |Statue of Washington [[Federal Hall]] in [[New York City]]}}
            {{image frame|content={{Photomontage
            | photo1a = Perú PZ.jpg{{!}}Freedom Monument, in Main Square
            of Trujillo city
            | photo2a = Húsares.jpg{{!}}"Húsares de Junín" avenue}}

            """
    assert solve(enwiki.images_in_templates, cache={revision_text: text}) == 5


def test_infobox_images():
    text = """
            {{Infobox artwork
            | image_file = (Явление Мессии) - Google Art Project.jpg
            | painting_alignment = Front
            | image_size         = 300px
            | title              = The Appearance of Christ Before the People
            | artist             = [[Alexander Andreyevich Ivanov]]
            | year               = 1837–1857
            | medium             = [[Oil painting|Oil]] on [[canvas]]
            | height_metric      = 540
            | width_metric       = 750
            | image_map          = Image map.svg
            | cover              = Artbook.pdf
            | metric_unit        = cm
            | imperial_unit      = in
            }}
            """
    assert solve(enwiki.infobox_images, cache={revision_text: text}) == 3

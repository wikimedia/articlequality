from revscoring.datasources.revision_oriented import revision
from revscoring.dependencies import solve

from .. import ptwiki

revision_text = revision.text


def test_cite_templates():
    text = """
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text. {{foo}} {{{cite}}}  {{sfn}}  {{Harvard citation}}

    I am a new paragraph.<ref>{{citar livro|title=The stuff}}</ref>
    {{Citar hat|ascii=_n_}}
    """
    assert solve(ptwiki.all_ref_tags, cache={revision_text: text}) == 3
    assert solve(ptwiki.all_cite_templates, cache={revision_text: text}) == 5


def test_infobox_templates():
    text = """
    {{Info pants|hats=2|pajams=23}}
    This is some text with a citation.<ref>{{cite lol|title=Made up}}</ref>
    This is some more text.

    I am a new paragraph.<ref>{{cite book|title=The stuff}}</ref>
    {{Cite hat|ascii=_n_}}
    """
    assert solve(ptwiki.infobox_templates, cache={revision_text: text}) == 1


def test_cn_templates():
    text = """
    {{Info pants|hats=2|pajams=23}}
    This is some text with a citation.{{Carece de fontes/bloco2}}
    This is some more text. {{foo}}

    I am a new paragraph.{{Carece de fontes/bloco|date=never}}

    I am a new paragraph.{{Carece de fontes|date=never}}
    """
    assert solve(ptwiki.cn_templates, cache={revision_text: text}) == 3


def test_main_article_templates():
    text = """
    This is some text with a citation.{{cn}}
    This is some more text. {{foo}}

    == Some section ==
    {{Artigo_principal|section}}

    I am a new paragraph.{{who|date=today}}
    """
    assert solve(ptwiki.main_article_templates,
                 cache={revision_text: text}) == 1


def test_paragraphs_without_refs_total_length():
    text = """
    Here is the first paragraph.
    It contains some references <ref>first reference</ref>.

    Here is second paragraph. One line with reference <ref>reference</ref>.

    Here is third paragraph.
    It has two lines, but no references.

    Here is fourth paragraph.
    It has two lines <ref name="foobar" />
    One of which has a reference.

    This paragraph is too short to count.

    Short line.<ref>last</ref><ref>One more reference</ref>
    """
    assert solve(ptwiki.paragraphs_without_refs_total_length,
                 cache={revision_text: text}) == 65


def test_image_links():
    text = """
            [[File:image.jpg|options|caption]]
            [[Ficheiro:sound.ogg|options|a sound]]
            [[Arquivo:display.svg|options|caption]]
            """
    assert solve(ptwiki.image_links, cache={revision_text: text}) == 3


def test_image_templates():
    text = """
            {{Scalable_image|Helsinki z00.jpg|400px|
            |alt=Panorama of city with mixture of story buildings}}

            {{Panorama
            |image   = File:Ushuaia_panorama_from_seaside_big.jpg}}

            {{imagem_vertical|Polarisation_(Circular).svg}}

            {{scalable_image|Dew on grass Luc Viatour.jpg}}

            {{Panorama 2
            | Image = image file name (don't need Files:)}}
            """
    assert solve(ptwiki.image_templates, cache={revision_text: text}) == 5


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
    assert solve(ptwiki.images_in_tags, cache={revision_text: text}) == 3


def test_image_in_templates():
    text = """
            {{imagem multipla
             | align = left
             | image1 = Frecklesmule.jpg
             | width1 = 143
             | alt1 = A mule
             | link1 = Mule
             | caption1 = A mule<br />(骡子 ''luózi'')}}
            """
    assert solve(ptwiki.images_in_templates, cache={revision_text: text}) == 1


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
    assert solve(ptwiki.infobox_images, cache={revision_text: text}) == 3

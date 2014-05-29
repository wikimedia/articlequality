from mwqual import TextClassifier
from mwqual import TextModel
from mwqual import languages

text = """
{{For|the card strategy game|Anachronism (game)}}
[[File:Leonardo da Vinci (1452-1519) - The Last Supper (1495-1498).jpg|thumb|right|450px|''[[The Last Supper (Leonardo)|The Last Supper]]'' by [[Leonardo da Vinci]], 1498, depicts  the apostles sitting  beside a long  table. This kind of table was unknown at the time and place of the [[Last Supper]].<ref>{{cite web|url=http://www.artinsociety.com/on-the-trail-of-the-last-supper.html|title=On the trail of the last supper|publisher=Aet in Society|accessdate=May 2012}}</ref>]]
An '''anachronism''' (from the [[Ancient Greek|Greek]] ἀνά ''ana'', "against" and χρόνος ''khronos'', "time"), is a [[chronology|chronological]] inconsistency in some arrangement, especially a juxtaposition of person(s), events, objects, or customs from different periods of time. The most common type of anachronism is an object misplaced in time, but it may be a verbal expression, a technology, a philosophical idea, a musical style, a material/textile, a custom or anything else associated with a particular period in time so that it is incorrect to place it outside its proper temporal domain.

==Art and literature==
Shakespeare's audience are not recorded as asking whether the [[University of Wittenberg]] had existed in [[Hamlet]]'s day, or whether clocks that [[striking clock|struck time]] were available in ''[[Julius Caesar (play)|Julius Caesar]]'s'' ancient Rome: Shakespeare portrayed [[Marcus Junius Brutus the Younger|Brutus]], plotting to assassinate [[Julius Caesar|Caesar]] in 44 BC, being interrupted by the striking of the clock,<ref>[http://shakespeare-navigators.com/JC_Navigator/JC_2_1.html#sd15 ''Julius Caesar'', Act 2, Scene 1, Line 192 - "''Clock strikes''"] or [http://shakespeare.mit.edu/julius_caesar/full.html#2.1.199 ''Julius Caesar'', Act 2, Scene 1 - "''Clock strikes''"]</ref> although [[ancient Rome]] was the era of the [[sundial]], with invention of the [[clock|mechanical clock]] dating from the 11th-13th centuries AD.<ref>{{cite web | url=http://www.antique-collectable-clock.com/who-invented-the-clock.html |title=Who invented the clock? |publisher=Antique-collectable-clock.com |date= |accessdate=2013-02-01}}</ref> In "[[A Midsummer Night's Dream]]", Shakespeare casually bestowed upon [[Theseus]]—a semi-legendary character dated to the misty time of the Second Millennium BC—the title of "[[Duchy of Athens|Duke of Athens]]", which derives from the Latin conquest the Byzantine Empire in the 13th Century AD.
"""

model = TextModel.from_file("enwiki.model.pkl")
langauge = langauges.get("en-us")

classifier = TextClassifier(model, language)

assessment, probs = classifier.classify(text)

print("assessment={0}".format(assessment))
print("probs={0}".format(probs))
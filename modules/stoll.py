# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Stoll quote module
"""
import random

def stoll(phenny, input):
	quotes = [
	"Allerdings muss ich gleich sagen: Bei mir beginnt die Mathematik, Physik und auch Geologie dort, wo das Hochschulstudium aufhört.",
	"Medizin ist Mathematik, Biologie ist Physik!",
	"Magie ist Physik durch Wollen!",
	"Der Mensch ist eine energetische Matrix.",
	"Der menschliche Zellkern ist gleich pures Licht, sprich: schwarze Sonnen.",
	"Wenn ein Mensch autogen sein Kraftfeld verstärkt, könnte er im Extremfall schweben. Also levitieren.",
	"Die Sonne ist KALT, da staunt ihr, wa?",
	"Wer weiß das? ... Wieder keiner!",
	"Im Prinzip brauchen wir nur drei Wissenschaften, um alles zu beschreiben: Physik. Mathematik. Philosophie.",
	"Und die Russen sind ja Waffentechnisch den Amerikanern weit überlegen. MUSS MAN WISSEN!",
	"...und das ist auch die Maschine, die entscheidend ist für Freie-Energie-Maschinen. Die muss man anzapfen entsprechend einem Implosions-Strudel. Das heißt, eine logarithmische Spirale raum-zeitlich betrachtet nach INNEN.",
	"Es gibt keine Zufälle, Das Wort 'Zufall' ist aus meinem Wortschatz gestrichen",
	"96 Flugzeuge * 60 Minuten * 14 Stunden * 40 Passagiere ergibt: 3.225.600 Passagiere pro Tag. PRO TAG! Das ist kein Science Fiction.",
	"Das hier ist nichts anderes als ein Strafplanet",
	"Der Selbsterhaltungstrieb der Zelle. Zur Erinnerung: [Die Zelle] ist ein Perpetuum Mobile, wie das Universum auch, ist ja klar.",
	"Wiederholung ist die Mutter der Weisheit",
	"Seit 10 Jahren wird der T-92 hergestellt. Ein modernster Panzer, russische Panzer mit Spitzengeschwindigkeit von 300 km/h",
	"Das Wort Zufall ist aus meinem Wortschatz gestrichen.",
	"Nukleare Strahlung lässt sich neutralisieren",
	"Magie ist Physik durch Volt",
	"Nikolai Tesla ist innerhalb von 5 Stunden mit deutschen Physikern zum Pluto geflogen um Gesteinsproben zu sammeln",
	"Man sollte mal Mikrowellenstrahler gegen die Love Parade einsetzen",
	"Es existiert keine Materie so wie diese beschrieben wird. Es existiert nur Bewegung oder Geschwindigkeit oder Schwingungen.",
	"Internet ist scheiße, da geh ich nicht rein",
    "Es existiert keine Materie, so wie diese gesehen und beschrieben wird, denn wir leben in einer Welt der Schwingungen und Frequenzen, also korrelierender Wirbelmechanismen",
    "Im Prinzip kann man sogar soweit abstrahieren: 'Alles ist nur Bewegung, Geschwindigkeit oder Schwingungen'",
    "Bindekräfte, welche die Materie zusammenhalten, sind Wirben bzw. Strudel, inklusive iher Ein- und Auswirbelungen",
    "Die Formel E = mc² ist in dieser Form falsch bzw. wird zumindest falsch verstanden!",
    "Die reinste aller Energieformen, das Licht, ist ein Element es Jenseitsraumes, auch wenn es in die materielle Welt hineinwirkt.",
    "Die Zeit ist gekommen, da die Menschheit darüber bescheid wissen muss, was einige Wenige -- aus niederen Beweggründen -- seit sehr langer Zeit verschweigen.",
    "Das Wort 'Kosmos' bedeutet ja zu deutsch letztlich auch nichts anderes als: Ordnung.",
    "Tachyoneutrinos beinhalten den Terminus Tachyon(en) und Neutrino(s). Ersterer enthält die wichtige limitierende physikalische Größe Zeit und Geschwindigkeit (=Bewegung) und letzterer einen 'Schwingungs-Frequenz-Wirbelquant'!",
    "Ein Atom z.B. ähnelt nicht nur einer Sprungfeder, sondern es verfügt auch über ähnliche Eigenschaften, außer dass es mit hoher Geschwindigkeit rotiert.",
    "Dieses Gebilde kennen wir nur als sogenanntes 'Schwarzes Loch'! So, wie aber beispielsweise Luzifer nicht der Teufel, sondern der Lichtbringer ist (lux = das Licht), so ist 'unser' Jenseits-Raum (Τ-freier Raum) pures Licht!!",
    "Eine große ΦM-Dichte führt der menschlichen Zelle soviel Energie zu, dass er nur langsam altert."
    "Wie im ... beschrieben, so ist die Zeit (T) physikalisch nichts weiter als universale Dichte in Korrelation mit der Raumbewegung.",
    "Implosions- und Expansionsstrudel sind zwar miteinander korrelierend, verfügen aber über eine unterschiedliche energetische Struktur."
    "Unser Universum ist das klassische 'Perpetuum Mobile' weil es aus sich selbst heruas existiert bzw. lebt.",
    "Da unser Universum ein ewig existierendes Zirkulationssystem darstellt, findet der sogenannte Urknall jederzeit statt.",
    "Die Masse eines Körpers entspricht dem Gesamt-Volumen seiner Atomkerne, also dem Gesamt-Volumen seiner 'Mini-Schwarzen Löcher'.",
    "Sein spezifisches Gewicht ist das Verhältnis des Volumens seiner 'Mini-Schwarzen Löcher' zu seinem Gesamtvolumen bei einer bestimmten Temperatur und relativ zu Wasser.",
    "Wie erwähnt, steckt in τ ein rechtsrotierender (zum jeweiligen imaginären Mittelpunkt zielender), spiralförmiger Kraftverlauf."
    "Die kleinen τ-freien Räume (die Atomkerne) erscheinen uns allgemein nur dann als Licht, wenn ihre Atome entbunden werden bzw. sich zerlegen.",
    "Zu beachten ist, dass wir in einer virtuellen Scheinwelt leben. Das bedeutet, dass wir nur die entsprechende Dichte der Schwingungen (Frequenzen) als unterschiedliche Aggregatzustände wahrnehmen!",
    "Strom ist nichts weiter als ausgeschiedene bzw. überschüssige Geschwindigkeit.",
    "Das Mini-Magnetfeld eines Atoms ist nichts weiter als sein Spin, der auch von τ weiter transportiert wird! Damit ist ein Magnet eine τ-Umwälzpumpe bzw. der Nachbau unseres Universums!",

	]

	phenny.say(random.choice(quotes))

stoll.commands = ['stoll']
stoll.priority = 'low'



if __name__ == '__main__':
   print __doc__.strip()

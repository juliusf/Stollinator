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
	"das wort zufall ist aus meinem wortschatz gestrichen",
	"nukleare strahlung laesst sich neutralisieren",
	"Magie ist Physik durch Volt",
	"Nikolai Tesla ist innerhalb von 5 Stunden mit deutschen Physikern zum Pluto geflogen um Gesteinsproben zu sammeln",
	"Man sollte mal Mikrowellenstrahler gegen die Love Parade einsetzen",
	"es existiert keine materie so wie diese beschrieben wird. es existiert nur bewegung oder geschwindigkeit oder schwingungen.",
	"Internet ist scheiße, da geh ich nicht rein",


	]

	phenny.say(random.choice(quotes))

stoll.commands = ['stoll']
stoll.priority = 'low'



if __name__ == '__main__':
   print __doc__.strip()

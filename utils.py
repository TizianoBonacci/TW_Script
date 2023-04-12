def converti_tempo(tempo_secondi):
    giorni = tempo_secondi // (24 * 3600)
    tempo_secondi %= (24 * 3600)
    ore = tempo_secondi // 3600
    tempo_secondi %= 3600
    minuti = tempo_secondi // 60
    return giorni, ore, minuti

<a href="https://www.casagrandecesi.edu.it/">
    <img src=".readme-files/logo-128.png" alt="Nightmare Machine" title="Nightmare Machine" align="right" height="128" />
</a>

# Nightmare Machine
> IIS "Casagrande-Cesi" Terni - Gamified Language Learning via Generative AI

[![Pedagogy](https://img.shields.io/badge/Subject-English_ESL-green.svg)](https://en.wikipedia.org/wiki/English_as_a_second_or_foreign_language)
[![Gamification](https://img.shields.io/badge/Mode-Immersive_Learning-purple.svg)](https://en.wikipedia.org/wiki/Gamification_of_learning)
[![Tech](https://img.shields.io/badge/AI-Gemini_2.0-magenta.svg)](https://deepmind.google/technologies/gemini/)

## Indice

- [Visione Didattica](#visione-didattica)
- [Meccaniche di Gioco](#meccaniche-di-gioco)
- [Obiettivi di Apprendimento](#obiettivi-di-apprendimento)
- [Installazione](#installazione)
- [Licenza](#licenza)

## Visione Didattica

**Nightmare Machine** trasforma la tradizionale lezione di inglese descrittivo in un'esperienza di *creative coding* immersiva.
Invece di correggere gli errori con la penna rossa, il sistema utilizza la **Generative AI** per "punire" o "premiare" visivamente lo studente: se la descrizione in inglese è ambigua o grammaticalmente scorretta, il mondo virtuale generato sarà caotico, incompleto o surreale (da qui il nome *"Nightmare Machine"*).

L'obiettivo è chiudere il feedback loop tra **linguaggio** e **realtà**: lo studente comprende l'importanza della precisione lessicale vedendo le conseguenze dirette delle proprie parole in uno spazio 3D navigabile.

## Meccaniche di Gioco

Il software agisce come un *Dungeon Master* digitale basato su tre fasi:

1.  **The Prompt (Input):** Lo studente riceve un task (es. *"Descrivi una scena spaventosa con tre lapidi e nebbia verde"*). Deve formulare la richiesta in inglese, prestando attenzione a preposizioni, aggettivi e vocabolario tecnico.
2.  **The Oracle (AI Feedback):** Prima di generare il mondo, l'AI (Google Gemini) analizza il testo e fornisce un feedback immediato sulla qualità della lingua (es. *"Attento: hai usato 'on' invece di 'above', la luna sarà appoggiata sul terreno!"*).
3.  **The Manifestation (Visual Reward):** Il codice A-Frame viene compilato. Lo studente indossa il visore (o usa il browser) ed "entra" nella frase che ha scritto.
    * *Successo:* La scena corrisponde all'immaginazione.
    * *Glitch/Nightmare:* La scena presenta errori bizzarri dovuti a descrizioni imprecise, spingendo al *try-and-retry*.

## Obiettivi di Apprendimento

Il progetto, sviluppato per le classi dell'IIS "Casagrande-Cesi", mira a potenziare:

* **Prompt Engineering as a Language Skill:** Imparare a comunicare con le intelligenze artificiali usando un inglese strutturato e preciso.
* **Lessico Spaziale e Descrittivo:** Uso intensivo di preposizioni di luogo (*next to, behind, floating above*) e aggettivi.
* **Pensiero Computazionale:** Comprendere come una descrizione astratta venga tradotta in oggetti, coordinate e attributi logici.

## Installazione

Il tool è pensato per essere eseguito in aula informatica o sul laptop del docente.

1. **Clona il repository:**
   ```bash
   git clone [https://github.com/casagrandecesi/nightmare-machine.git](https://github.com/casagrandecesi/nightmare-machine.git)
   cd nightmare-machine
   ```
2. **Installa le dipendenze:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configurazione:** Crea un file `settings.py` nella root del progetto e inserisci la tua chiave:
    ```python
    API_KEY = "LA_TUA_CHIAVE_GOOGLE_AI_STUDIO"
    ```
4. **Avvio il gioco:**
    ```bash
    python nightmaremachine.py
    ```

## Licenza

Il software contenuto in questo repository è distribuito secondo i termini della 2-clauses BSD license.
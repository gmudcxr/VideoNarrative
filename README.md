# Video Narrative

Generate Narrative via TTS For Paper Video Demo

## Usage:

- Fill content in `input.txt` file. ONE line outputs one SINGLE wav file.

Example

```text
Hello World.

This is the second voice file.

This is the third voice file.
```

- Run `main.py`

- See output in `./output/`

    - 'Sentences.txt' is the sentences beginning with the number, which can help you find the corresponding sound file.
    - 'Sentence_{number}.wav' is the wav file.

Example

```text
1	Hello World.
2	This is the second voice file.
3	This is the third voice file.   
``` 

Corresponding to

```
Sentence_1.wav
Sentence_2.wav
Sentence_3.wav
```

## Voice Settings:

- Change `line 11,12,13` in `main.py`

```python
### Voice Settings
rate = 125
volume = 1.0
voice = Voices.Male  # Voices.Female.
###
```

For more details regarding the voice settings, please refer to [pyttsx3](https://pypi.org/project/pyttsx3/).
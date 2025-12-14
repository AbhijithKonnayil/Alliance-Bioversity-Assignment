import sys

from mock_audio import MOCK_AUDIO
from rules import RULES


def generate_mock_transcription(audio_file):
    transcription = MOCK_AUDIO.get(audio_file, "")
    return transcription


def generate_follow_up_questions(transcription):
    for rule in RULES:
        if any(keyword in transcription for keyword in rule["keywords"]):
            return rule["followups"][:2]

    return ["Can you describe the problem in more detail?"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file>")
        return
    user_input = sys.argv[1]
    transcription = generate_mock_transcription(user_input)
    print("\nTranscription:", transcription)
    questions = generate_follow_up_questions(transcription)
    print("\nFollow-up Questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}: {q}")


if __name__ == "__main__":
    main()

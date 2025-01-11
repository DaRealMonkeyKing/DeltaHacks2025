from gpt4all import GPT4All
import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
warnings.filterwarnings("ignore", message=".*torch.load.*weights_only.*")

def interpret_mp3(file):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(file)
        print(f'The text in video: \n {result["text"]}')
        return result

    except FileNotFoundError:
        print("File could not be found")

    # except whisper.audio.AudioDecodeError:
    #     print("Unable to decode audio")

    except Exception as e:
        print(f"Unexpected error {e}")

interpret_mp3("AudioTests/audioTest.mp3")
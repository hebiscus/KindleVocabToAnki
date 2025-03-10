import tempfile


def save_temp_file(vocab_file):
    if vocab_file and vocab_file.name.endswith('.db'):
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in vocab_file.chunks():
                    temp_file.write(chunk)
                return temp_file.name
        except Exception as e:
            raise Exception(f"Error saving the uploaded file: {str(e)}")
    else:
        raise Exception("Invalid file format. Only .db files are allowed.")

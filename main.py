import os


if __name__ == '__main__':
    with open('static_files/analyser.html') as f:
        template = f.read()

    for log_fname in os.listdir('logs'):
        with open(f'logs/{log_fname}') as log_file:
            with open(f'generated_files/{log_fname}.html', 'w') as f:
                f.write(template.format(log_file.read()))



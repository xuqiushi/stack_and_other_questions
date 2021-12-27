import re


class LineReplacer(object):
    def __init__(self, replace_word, max_word_count):
        self.word_index = 1
        self.word_to_replace = replace_word
        self.max_word_count = max_word_count

    @property
    def word_regex(self):
        return re.compile(f"(?<=[^a-zA-Z0-9]){self.word_to_replace}(?=[^a-zA-Z0-9])")

    def replace_function(self, match):
        current_index = self.word_index
        if self.word_index < self.max_word_count:
            self.word_index += 1
        else:
            self.word_index = 1
        return f"{match.group()}{current_index}"

    def replace_file(self, input_file_path, output_file_path):
        output = open(output_file_path, "w")
        with open(input_file_path, "r") as f:
            for line in f.readlines():
                new_line = self.word_regex.sub(self.replace_function, line)
                output.write(new_line)
        output.close()


if __name__ == "__main__":
    replacer = LineReplacer("boss", 60)
    replacer.replace_file("data/replace_in_file.txt", "output.txt")

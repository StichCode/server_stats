class Template_info_system:

    def __init__(self, info_about_system: list):
        self.data = info_about_system
        self.max_str = self.max_len_words()

    def __repr__(self):
        return self.template_message_ram()

    def template_message_ram(self):
        """ Beautiful ram output """
        result = ""
        for el in self.data:
            # pid - 0, ram - 1, name - 2,  time works - 3, cmd line - 4, cpu - 5
            pid = self.default_len_word(el[0], self.max_str[0])
            ram = self.default_len_word(el[1], self.max_str[1])
            name = self.default_len_word(el[2], self.max_str[2])
            time = self.default_len_word(el[3], self.max_str[3])
            # cmd = self.default_len_word(el[4], self.max_str[4])
            cpu = self.default_len_word(el[5], self.max_str[5])
            result += f"{pid} {ram} %  {cpu} {name} {time}\n"
        return result

    def max_len_words(self):
        """ Create a list with the maximum length of each word """
        max_pid = max_ram = max_name = max_time = max_cmd = max_cpu = 0
        for el in self.data:
            max_pid = max(max_pid, len(el[0]))
            max_ram = max(max_ram, len(el[1]))
            max_name = max(max_name, len(el[2]))
            max_time = max(max_time, len(el[3]))
            max_cmd = max(max_cmd, len(el[4]))
            max_cpu = max(max_cpu, len(el[5]))
        return [max_pid, max_ram, max_name, max_time, max_cmd, max_cpu]

    @staticmethod
    def default_len_word(str_data, max_len):
        """ Searches for a word with maximum length and makes it the standard for others """
        if isinstance(str_data, float):
            print(str_data)
        if len(str_data) < max_len:
            for i in range(max_len - len(str_data)):
                str_data += " "
        return str_data


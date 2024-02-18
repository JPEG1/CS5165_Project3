import os
import socket
from collections import Counter

class TextAnalyzer(object):
    """ Class Variables & Constants """
    directory: str = None       # directory where the text files are located (same directory in which this Python script exists)
    text_files: list = None     # list of .txt files enumerated in the current working directory
    ip_address: str = None      # IP address of the machine running this Python script
    total_words: int = None     # total number of words in all text files
    top_words_if = None
    top_words_limerick = None

    """ Class Initializer """
    def __init__(self):
        self.directory = os.getcwd()    # gets current working directory
    # end of initializer

    """ Class Methods """
    def run_text_analysis(self):
        '''
        This method performs the text analysis and finds the top 3 most common words.
        '''
        # call helper method to list all text files in the current working directory
        self.list_text_files()
        print("List of text files:", self.text_files)

        # read and count words in each text file
        self.total_words = 0
        for file_name in self.text_files:
            file_path = os.path.join(self.directory, file_name)
            file_word_count = self.count_words(file_path)
            print(f"Total words in {file_name:<20}-{file_word_count:>10}")
            self.total_words += file_word_count  # increments total_words
        # end of for loop

        # display the grand total number of words
        print(f"Grand total number of words:{self.total_words:>10}")

        # find top 3 words with maximum counts in IF.txt
        print("\nTop 3 words in IF.txt:")
        self.top_words_if = self.find_top_words("IF.txt", self.top_words_if)

        # find top 3 words with maximum counts in Limerick-1.txt
        print("\nTop 3 words in Limerick-1.txt:")
        self.top_words_limerick = self.find_top_words("Limerick-1.txt", self.top_words_limerick)

        # find IP address of the machine
        self.ip_address = socket.gethostbyname(socket.gethostname())    # luckily, the Python socket module has a built-in function which makes this easy
        print(f"\nIP Address:{self.ip_address:>20}")
    # end of run_text_analysis() method
        
    def output_results(self):
        '''
        This method creates and formats the output, sending it to both the 'results.txt' text file and the console.
        '''
        output_file_path = os.path.join(self.directory, "output", 'result.txt')
        output_file = open(output_file_path, "w")   # opens the output file for writing
        output_file.write("List of text files:" + ', '.join(self.text_files) + '\n')
        for file_name in self.text_files:
            file_path = os.path.join(self.directory, file_name)
            file_word_count = self.count_words(file_path)
            output_file.write(f"Total words in {file_name:<20}-{file_word_count:>10}\n")
        # end of for loop
        
        output_file.write(f"Grand total number of words:{str(self.total_words):>10}\n")
        output_file.write("\n")     # writes an empty line of space to output file before next section of outputs
        output_file.write("Top 3 words in IF.txt:\n")
        for word, count in self.top_words_if:
            output_file.write(f"{word:<10}-{count:>10}\n")
        # end of for loop
        
        output_file.write("\n")     # writes an empty line of space to output file before next section of output
        output_file.write("Top 3 words in Limerick-1.txt:\n")
        for word, count in self.top_words_limerick:
            output_file.write(f"{word:<10}-{count:>10}\n")
        # end of for loop
        
        output_file.write(f"\nIP Address:{self.ip_address:>20}")
        output_file.close()     # closes the output file
    # end of output_results() method

    """ Class Helper Methods """
    def list_text_files(self):
        '''
        This method lists all text files in a directory.
        '''
        self.text_files = [file for file in os.listdir(self.directory) if file.endswith('.txt')]  # uses list comprehension to retrieve a list of ONLY .txt files in the current directory
    # end of list_test_files() method
        
    def find_top_words(self, file_path, top_words):
        file_path = os.path.join(self.directory, file_path)
        top_words = self.top_words(file_path)

        # print top 3 words to console
        for word, count in top_words:
            print(f"{word:<10}-{count:>10}")
        # end of for loop
            
        return top_words
    # end of find_top_words() method

    def count_words(self, file_path):
        '''
        This method counts the number of words in a text file.
        '''
        txt_file = open(file_path, "r") # opens the file in read only mode
        words = txt_file.read().split() # read entire file, and split into words (split by spaces)
        txt_file.close()            # closes the text file
        return len(words)   # returns the number of words
    # end of count_words() method

    def top_words(self, file_path):
        '''
        This method finds the top 3 most common words in a text file.
        '''
        txt_file = open(file_path, "r") # opens the file in read only mode
        words = txt_file.read().split() # read entire file, and split into words (split by spaces)
        word_counts = Counter(words)    # luckily, Python has a 'Counter' class which makes this task extremely easy
        most_common_words = word_counts.most_common(3)  # calls a method which returns the n most common words (where n is the argument passed in)
        txt_file.close()            # closes the text file
        return most_common_words    # returns the most common words
    # end of top_words() method
# end of TextAnalyzer() class

# Application Starts Here
if (__name__ == '__main__'):
    ta = TextAnalyzer()     # creates instance of the TextAnalysizer() class
    ta.run_text_analysis()  # calls method which runs text analysis
    ta.output_results()     # calls method which formats an output for the user
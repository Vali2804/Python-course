class LibraryItem:
    def __init__(self, title, author, call_number):
        self.title = title
        self.author = author
        self.call_number = call_number
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already in the library.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Call Number: {self.call_number}")
        print(f"Status: {'Checked Out' if self.checked_out else 'Available'}")


class Book(LibraryItem):
    def __init__(self, title, author, call_number, num_pages):
        super().__init__(title, author, call_number)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, director, call_number, release_year):
        super().__init__(title, director, call_number)
        self.director = director
        self.release_year = release_year

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Release Year: {self.release_year}")


class Magazine(LibraryItem):
    def __init__(self, title, publisher, call_number, issue_num):
        super().__init__(title, publisher, call_number)
        self.publisher = publisher
        self.issue_num = issue_num

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}")
        print(f"Issue Number: {self.issue_num}")

def main():
    library_items = [Book("Fram Ursul Polar", "Cezar Petrescu", "1234", 150), DVD("Toate pînzele sus", "Mircea Mureșan", "5678", 1977), Magazine("Time", "Time Inc.", "9101", 1)]
    for library_item in library_items:
        library_item.display_info()
        library_item.check_out()
        library_item.return_item()
        print()

if __name__ == "__main__":
    main()

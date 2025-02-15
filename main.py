import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc

#Initializing the connection to SQL
def config():
    global cursor, conn
    conn = pyodbc.connect('Driver={SQL Server}; Server=MariaPC; Database=lms; Trusted_Connection=yes;  Connection Timeout=100;')
    cursor = conn.cursor()

#Adding Login Page
def main():
    login_page()

#Adding main page
def open_main_page(login_window):
    login_window.destroy()

    main_page = tk.Tk()
    main_page.title("Main Page")
    main_page.geometry("400x300")

    # Labels
    welcome_label = tk.Label(main_page, text="Welcome to the Library Management System")
    welcome_label.pack(pady=10)

    # Buttons
    show_all_tables_button = tk.Button(main_page, text="Show Tables", command=show_all_tables)
    show_all_tables_button.pack(pady=10)

    search_all_tables_button = tk.Button(main_page, text="Search Tables", command=search_all_tables)
    search_all_tables_button.pack(pady=10)

    delete_from_tables_button = tk.Button(main_page, text="Delete from Tables", command=delete_from_tables)
    delete_from_tables_button.pack(pady=10)

    add_data_button = tk.Button(main_page, text="Add data", command=add_data)
    add_data_button.pack(pady=10)

    back_button = tk.Button(main_page, text="Back", command=lambda: back_to_login(main_page))
    back_button.pack(pady=10)

    main_page.mainloop()

#defining show all tables button
def show_all_tables():
    show_tables_window = tk.Tk()
    show_tables_window.title("Show All Tables")
    show_tables_window.geometry("400x300")

    # Buttons for each table
    admins_button = tk.Button(show_tables_window, text="Admins", command=show_admins)
    admins_button.grid(row=0, column=0, padx=30, pady=10)

    authors_button = tk.Button(show_tables_window, text="Authors", command=show_authors)
    authors_button.grid(row=0, column=1, padx=30, pady=10)

    books_button = tk.Button(show_tables_window, text="Books", command=show_books)
    books_button.grid(row=0, column=2, padx=30, pady=10)

    late_fees_button = tk.Button(show_tables_window, text="Late Fees", command=show_late_fees)
    late_fees_button.grid(row=1, column=0, padx=30, pady=10)

    loans_button = tk.Button(show_tables_window, text="Loans", command=show_loans)
    loans_button.grid(row=1, column=1, padx=30, pady=10)

    members_button = tk.Button(show_tables_window, text="Members", command=show_members)
    members_button.grid(row=1, column=2, padx=30, pady=10)

    publishers_button = tk.Button(show_tables_window, text="Publishers", command=show_publishers)
    publishers_button.grid(row=2, column=0, padx=30, pady=10)

    transactions_button = tk.Button(show_tables_window, text="Transactions", command=show_transactions)
    transactions_button.grid(row=2, column=1, padx=30, pady=10)

    back_button = tk.Button(show_tables_window, text="Back", command=show_tables_window.destroy)
    back_button.grid(row=3, column=0, columnspan=3, pady=40)

    show_tables_window.mainloop()

#Showing all admins
def show_admins():
    config()
    query = f"SELECT * FROM Admins"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Admins Data")
    popup.geometry("400x300")

    # Create a text widget to display data and column names
    text_widget = tk.Text(popup, wrap="none")

    # Display column names
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")

    # Display data
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")

    popup.mainloop()

#Showing authors
def show_authors():
    config()
    query = f"SELECT * FROM Authors"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Authors Data")
    popup.geometry("700x300")

    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")

    popup.mainloop()

#Showing books, need to join on authors to show Author Name
def show_books():
    config()
    query = " SELECT b.BookID, b.Title, a.AuthorName, b.ISBN, b.PubisherID,  b.Genre,   b.Quantity, b.AvailabilityStatus FROM books b JOIN authors a ON b.AuthorID = a.AuthorID; "
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Books Data")
    popup.geometry("700x300")

    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

#Using similar functions for each button
def show_late_fees():
    config()
    query = f"SELECT * FROM latefees"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Late fees Data")
    popup.geometry("700x300")


    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

def show_loans():
    config()
    query = f"SELECT * FROM Loans"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Loans Data")
    popup.geometry("700x300")
    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

def show_members():
    config()
    query = f"SELECT * FROM Members"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Members Data")
    popup.geometry("700x300")
    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

def show_publishers():
    config()
    query = f"SELECT * FROM Publishers"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("Publishers Data")
    popup.geometry("700x300")

    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

def show_transactions():
    config()
    query = f"SELECT * FROM transactions"
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    conn.close()

    popup = tk.Tk()
    popup.title("transactions Data")
    popup.geometry("700x300")
    text_widget = tk.Text(popup, wrap="none")
    text_widget.insert("1.0", "\t\t".join(column_names) + "\n")
    text_widget.insert("2.0", "\n".join(["\t\t".join(map(str, row)) for row in data]))
    text_widget.pack(expand=True, fill="both")
    popup.mainloop()

#Defining search function and button based on keyword
def search_all_tables():
    search_window = tk.Tk()
    search_window.title("Search Tables")
    search_window.geometry("400x300")

    # Radio buttons for each table
    selected_table = tk.StringVar()

    books_button = tk.Radiobutton(search_window, text="Books", variable=selected_table, value="Books")
    books_button.grid(row=0, column=0, padx=30, pady=10)

    authors_button = tk.Radiobutton(search_window, text="Authors", variable=selected_table, value="Authors")
    authors_button.grid(row=0, column=1, padx=30, pady=10)

    members_button = tk.Radiobutton(search_window, text="Members", variable=selected_table, value="Members")
    members_button.grid(row=0, column=2, padx=30, pady=10)


    # Textbox for search input
    search_textbox_label = tk.Label(search_window, text="Search Keyword:")
    search_textbox_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    search_textbox = tk.Entry(search_window)
    search_textbox.grid(row=1, column=1, pady=10, padx=10)

    # Search button
    searchbooks_button = tk.Button(search_window, text="Search Books", command=lambda: perform_searchbooks(search_textbox.get()))
    searchbooks_button.grid(row=2, column=0, padx=10, pady=20)

    searchauthors_button = tk.Button(search_window, text="Search Authors", command=lambda: perform_searchauthors(search_textbox.get()))
    searchauthors_button.grid(row=2, column=1, padx=10, pady=20)

    searchmembers_button = tk.Button(search_window, text="Search Members", command=lambda: perform_searchauthors(search_textbox.get()))
    searchmembers_button.grid(row=2, column=2, padx=10, pady=20)

    back_button = tk.Button(search_window, text="Back", command=search_window.destroy)
    back_button.grid(row=3, column=1, padx=10, pady=20)

    search_window.mainloop()

#Define the search query for each table (books, authors, members)
def perform_searchbooks(search_text):
    config()
    query = f"SELECT * FROM Books WHERE Title = ?"
    cursor.execute(query, (search_text,))
    search_result = cursor.fetchall()
    conn.close()

    if search_result:
        show_search_result(search_result)
    else:
        messagebox.showinfo("No Results", "No results found.")

def perform_searchauthors(search_text):
    config()
    query = f"SELECT * FROM Authors WHERE AuthorName = ?"
    cursor.execute(query, (search_text,))
    search_result = cursor.fetchall()
    conn.close()

    if search_result:
        show_search_result(search_result)
    else:
        messagebox.showinfo("No Results", "No results found.")

def perform_searchmembers(search_text):
    config()
    query = f"SELECT * FROM Members WHERE MembersName = ?"
    cursor.execute(query, (search_text,))
    search_result = cursor.fetchall()
    conn.close()

    if search_result:
        show_search_result(search_result)
    else:
        messagebox.showinfo("No Results", "No results found.")

def show_search_result(result):
    result_window = tk.Tk()
    result_window.title("Search Result")
    result_window.geometry("700x200")

    # Create a text widget to display search result
    text_widget = tk.Text(result_window, wrap="none")

    # Display data
    text_widget.insert("1.0", "\n".join(["\t\t".join(map(str, row)) for row in result]))
    text_widget.pack(expand=True, fill="both")
    result_window.mainloop()

#Define delete data button
def delete_from_tables():
    delete_tables_window = tk.Tk()
    delete_tables_window.title("Delete Data from Tables")
    delete_tables_window.geometry("450x300")

    # Buttons for each table
    books_button = tk.Button(delete_tables_window, text="Delete Books",
                             command=lambda: open_delete_data_window(delete_tables_window, "Books", delete_from_books))
    books_button.grid(row=0, column=0, padx=20, pady=10)

    authors_button = tk.Button(delete_tables_window, text="Delete Authors",
                               command=lambda: open_delete_data_window(delete_tables_window, "Authors",
                                                                       delete_from_authors))
    authors_button.grid(row=0, column=1, padx=20, pady=10)

    loans_button = tk.Button(delete_tables_window, text="Delete Loans",
                             command=lambda: open_delete_data_window(delete_tables_window, "Loans", delete_from_loans))
    loans_button.grid(row=0, column=2, padx=20, pady=10)

    transactions_button = tk.Button(delete_tables_window, text="Delete Transactions",
                                    command=lambda: open_delete_data_window(delete_tables_window, "Transactions",
                                                                            delete_from_transactions))
    transactions_button.grid(row=1, column=0, padx=20, pady=10)

    publishers_button = tk.Button(delete_tables_window, text="Delete Publishers",
                                  command=lambda: open_delete_data_window(delete_tables_window, "Publishers",
                                                                          delete_from_publishers))
    publishers_button.grid(row=1, column=1, padx=20, pady=10)

    members_button = tk.Button(delete_tables_window, text="Delete Members",
                               command=lambda: open_delete_data_window(delete_tables_window, "Members",
                                                                       delete_from_members))
    members_button.grid(row=1, column=2, padx=20, pady=10)

    latefees_button = tk.Button(delete_tables_window, text="Delete Late Fees",
                                command=lambda: open_delete_data_window(delete_tables_window, "Late Fees",
                                                                        delete_from_late_fees))
    latefees_button.grid(row=2, column=1, padx=20, pady=10)

    # Back button
    back_button = tk.Button(delete_tables_window, text="Back", command=delete_tables_window.destroy)
    back_button.grid(row=4, column=1, padx=20, pady=20)

    delete_tables_window.mainloop()

#opening the deletion window containing each table's button
def open_delete_data_window(previous_window, table_name, delete_function):
    previous_window.destroy()

    delete_data_window = tk.Tk()
    delete_data_window.title(f"Delete Data from {table_name}")

    # Textbox for keyword input
    keyword_label = tk.Label(delete_data_window, text="Enter Keyword or ID to delete:")
    keyword_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

    keyword_textbox = tk.Entry(delete_data_window, width=30)
    keyword_textbox.grid(row=0, column=1, pady=10, padx=10)

    # Add back button
    back_button = tk.Button(delete_data_window, text="Back", command=lambda: delete_data_window.destroy())
    back_button.grid(row=3, column=1, columnspan=2, pady=20)

    # Add delete data button
    delete_data_button = tk.Button(delete_data_window, text="Delete",
                                   command=lambda: delete_function(keyword_textbox.get()))
    delete_data_button.grid(row=3, column=0, columnspan=2, pady=10)

    delete_data_window.mainloop()

#Defining the query for each delete button
def delete_from_books(keyword):
    config()
    try:
        query = "DELETE FROM Books WHERE Title LIKE ? OR BookID = ?"
        cursor.execute(query, ('%' + keyword + '%', keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()

#Define deleting for authors
def delete_from_authors(keyword):
    config()
    try:
        query = "DELETE FROM Authors WHERE AuthorName LIKE ? OR AuthorID = ?"
        cursor.execute(query, ('%' + keyword + '%', keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()

#USing similar functions for other tables
def delete_from_loans(keyword):
    config()
    try:
        query = "DELETE FROM Loans WHERE LoanID = ?"
        cursor.execute(query, (keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()


def delete_from_transactions(keyword):
    config()
    try:
        query = "DELETE FROM Transactions WHERE TransactionID = ?"
        cursor.execute(query, (keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()


def delete_from_publishers(keyword):
    config()
    try:
        query = "DELETE FROM Publishers WHERE PublisherName LIKE ? OR PublisherID = ?"
        cursor.execute(query, ('%' + keyword + '%', keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()


def delete_from_members(keyword):
    config()
    try:
        query = "DELETE FROM Members WHERE membersName LIKE ? OR MemberID = ?"
        cursor.execute(query, ('%' + keyword + '%', keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()


def delete_from_late_fees(keyword):
    config()
    try:
        query = "DELETE FROM Latefees WHERE LatefeeID = ?"
        cursor.execute(query, (keyword))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed. Error: {str(e)}")
    finally:
        conn.close()

#Defining the add data button to insert data
def add_data():
    add_tables_window = tk.Tk()
    add_tables_window.title("Add Data to Tables")
    add_tables_window.geometry("400x300")

    # Buttons for each table
    books_button = tk.Button(add_tables_window, text="Add Books",
                             command=lambda: open_add_data_window(add_tables_window, "Books"))
    books_button.grid(row=0, column=0, padx=20, pady=10)

    authors_button = tk.Button(add_tables_window, text="Add Authors",
                               command=lambda: open_add_data_window(add_tables_window, "Authors"))
    authors_button.grid(row=0, column=1, padx=20, pady=10)

    members_button = tk.Button(add_tables_window, text="Add Members",
                               command=lambda: open_add_data_window(add_tables_window, "members"))
    members_button.grid(row=0, column=2, padx=20, pady=10)

    loans_button = tk.Button(add_tables_window, text="Add Loans",
                               command=lambda: open_add_data_window(add_tables_window, "Loans"))
    loans_button.grid(row=1, column=0, padx=20, pady=10)

    transactions_button = tk.Button(add_tables_window, text="Add Transactions",
                               command=lambda: open_add_data_window(add_tables_window, "Transactions"))
    transactions_button.grid(row=1, column=1, padx=20, pady=10)

    latefees_button = tk.Button(add_tables_window, text="Add Late Fees",
                               command=lambda: open_add_data_window(add_tables_window, "Late Fees"))
    latefees_button.grid(row=1, column=2, padx=20, pady=10)

    publishers_button = tk.Button(add_tables_window, text="Add Publishers",
                               command=lambda: open_add_data_window(add_tables_window, "Publishers"))
    publishers_button.grid(row=2, column=0, padx=20, pady=10)

    admins_button = tk.Button(add_tables_window, text="Add Admins",
                               command=lambda: open_add_data_window(add_tables_window, "Admins"))
    admins_button.grid(row=2, column=1, padx=20, pady=10)


    # Back button
    back_button = tk.Button(add_tables_window, text="Back", command=add_tables_window.destroy)
    back_button.grid(row=3, column=1, padx=20, pady=20)

    add_tables_window.mainloop()

#opening the new insert data window
def open_add_data_window(previous_window, table_name):
    previous_window.destroy()

    add_data_window = tk.Tk()
    add_data_window.title(f"Add Data to {table_name}")
    add_data_window.geometry("700x300")

    # Textbox for data input
    format_label = tk.Label(add_data_window, text=f"Format: {get_table_format(table_name)}")
    format_label.grid(row=0, column=0, columnspan=2, pady=10)

    data_textbox_label = tk.Label(add_data_window, text="Enter data (comma-separated, fill according to format):")
    data_textbox_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    data_textbox = tk.Entry(add_data_window, width=50)
    data_textbox.grid(row=1, column=1, pady=10, padx=10)

    # Add back button
    back_button = tk.Button(add_data_window, text="Back",
                            command=lambda: back_to_add_tables(add_data_window, previous_window))
    back_button.grid(row=2, column=1, columnspan=2, pady=20)

    # Add data button
    add_data_button = tk.Button(add_data_window, text="Add Data",
                                command=lambda: insert_data(table_name, data_textbox.get()))
    add_data_button.grid(row=2, column=0, columnspan=2, pady=10)

    add_data_window.mainloop()


#using specific formats to insert data
def get_table_format(table_name):
    # Define the expected format for each table
    table_formats = {
        "Books": "BookID, AuthorID, title, ISBN, PubisherID, Genre, PublicationDate, Quantity, AvailabilityStatus",
        "Authors": "AuthorID, AuthorName, BirthDate, Nationality, OtherRelevantInformation",
        "Members": "MemberID, MembersName, MembersAddress, Email, PhoneNumber, MemberShipType",
        "Loans": "LoanID, MemberID, BookID, LoanDate, DueDate, ReturnDate",
        "Transactions": "TransactionID, MemberID, BookID, TransactionType, TransactionDate, DueDate, ReturnDate",
        "Late Fees": "LateFeeID, TransactionID, Amount, PaymentStatus, PaymentDate",
        "Publishers": "PublisherID, PublisherName, PublisherAddress, ContactInformation",
        "Admins": "AdminID, UserName, Password"
    }
    return table_formats.get(table_name, "")

#using the inserted string as a query to write data into tables
def insert_data(table_name, data):
    config()
    columns = get_table_format(table_name).split(", ")
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"

    try:
        cursor.execute(query, tuple(data.split(", ")))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to insert data. Error: {str(e)}")
    finally:
        conn.close()

#adding the back button function
def back_to_add_tables(current_window, previous_window):
    current_window.destroy()
    add_data()


def back_to_login(main_page):
    main_page.destroy()
    login_page()

#making the login page
def login_page():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x200")

    # Username label and entry
    username_label = tk.Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, pady=30, padx=40, sticky="w")

    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, pady=10, padx=10)

    # Password label and entry
    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, pady=10, padx=40, sticky="w")

    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, pady=10, padx=10)

    # Login button
    login_button = tk.Button(login_window, text="Login", command=lambda: login_attempt(login_window, username_entry, password_entry))
    login_button.grid(row=2, column=1, pady=20, padx=10, sticky="w")

    login_window.mainloop()

#check the entered data with the admins table
def validate_login(username, password):
    config()
    query = "SELECT * FROM admins WHERE UserName = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

#get the input text and validate the user
def login_attempt(login_window, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    user = validate_login(username, password)

    if user:
        open_main_page(login_window)
    else:
        messagebox.showerror("Error", "Incorrect username or password.")

if __name__ == '__main__':
    main()
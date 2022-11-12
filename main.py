# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# print("U+1F982")

from bot_commands import *



app = ApplicationBuilder().token("5466100628:AAF6NEj5TVg-6ZDBTNhfH_5CH_5sLR_e8bI").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("diff", diff_command))
app.add_handler(CommandHandler("del", del_command))
print("Gut")
app.run_polling()


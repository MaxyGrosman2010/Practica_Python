import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key = config.api_key
    print("[bold red]>Practice Chat GPT API with Python[/bold red]")
    table = Table("Command", "Description")
    table.add_row("exit", "Closes the program")
    table.add_row("new", "Creates a new conversation")
    print(table)
#Setting up the CGPT
#Roles:
# -system: The kind of function it will have as an assistant
# -user: The way the user connects with CGPT
# -assistant: The way CGPT will remember the whole conversation.
    context = {"role": "system",
               "content": "You are an assistant with knowledge about videogames"}
    messages = [context]

    while True:
        content = __prompt()
        if content == "new":
            print("[bold yellow]Lets begin a new chat[/bold yellow]")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= messages)
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})
        print(f"[bold blue]>\nMessage: {response_content}\n\nRemaining usages: {response.usage}[/bold blue]")

def __prompt() -> str:
    prompt = typer.prompt("\nWhat do you want to ask?")
    if prompt == "exit":
        exit = typer.confirm("Are you sure you want to exit?")
        if exit:
            print("Goodbye!")
            raise typer.Abort()
        return __prompt()
    # elif prompt == "new":messages = context

    return prompt

if __name__ == "__main__":
    typer.run(main)
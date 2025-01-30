import asyncio

import reflex as rx
import random as rnd
import time


class State(rx.State):
    language:str="C#"
    languages=[
        "C#",
        "C#",
        "Python",
        "JavaScript",
        "TypeScript",
        "Rust",
        "Python",
        "Python",
        "Mojo",
        "Java",
        "C++",
        "C",
        "Haskell",
        "Python",
        "Fortran",
        "Piet",
        "C--",
        "Go",
        "Visual Basic",
        "Kotlin",
        "Swift",
        "VBA",
        "ActionScript",
        "Delphi",
    ]



    async def pick(self):
        language=rnd.choice(self.languages)
        yield
        for x in range(5):
            await asyncio.sleep(0.1)
            lang = rnd.choice(self.languages)
            for i in range(len(lang)+1):
                await asyncio.sleep(0.05)
                self.language="$> "+lang[:i]+(" //" if i % 2 == 0 else "")
                yield
            yield
        for i in range(len(language) + 1):
            await asyncio.sleep(0.1)
            self.language = "$> "+language[:i]+" //"
            yield

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.card(

            rx.container(
                rx.vstack(
                    rx.heading(
                        "Language Roulette!",
                        size="9",
                        color_scheme="indigo"
                    ),
                    rx.heading(
                        rx.code(
                            State.language,
                            size="9",
                            color_scheme="indigo",

                        ),
                        size="9"
                    ),
                    rx.button(
                        rx.text("pick a language"),
                        size="4",
                        color_scheme="indigo",
                        on_click=State.pick,
                        variant="solid"
                    ),
                    spacing="9",
                    justify="center",
                    min_height="85vh",
                    min_width="90wh",
                ),
                padding="20px"
            ),
            size="1",
            variant="surface"
        ),
        padding="15px",
    )


app = rx.App()
app.add_page(index)

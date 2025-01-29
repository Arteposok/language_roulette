"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random as rnd


class State(rx.State):
    language:str="C#"
    languages=[
        "C#",
        "C#",
        "C#",
        "Python",
        "Python",
        "JavaScript",
        "JavaScript",
        "TypeScript",
        "Rust",
        "Python",
        "Rust",
        "Python",
        "Mojo",
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
        "Python",
        "Swift",
        "VBA",
        "ActionScript",
        "Delphi",
    ]

    def pick(self):
        self.language=rnd.choice(self.languages)


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
                            color_scheme="indigo"
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

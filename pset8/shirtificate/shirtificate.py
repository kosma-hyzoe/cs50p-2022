from fpdf import FPDF


def main():
    name = input("Your name: ")

    pdf = Shirtificate(name)
    pdf.output("shirtificate.pdf")


class Shirtificate(FPDF):

    def __init__(self, name: str):
        super().__init__(orientation="portrait", format="A4")
        self.add_page()
        self.image("shirtificate.png", x=0, y=50)
        self.body(name)

    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 10, "CS50 Shirtificate", align="C")

    def body(self, name):
        self.ln()
        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 200, f"{name} took CS50", align="C")


if __name__ == '__main__':
    main()

import os
import re

class Markdown:
    @staticmethod
    def toMarkdown(file) -> None:
        if not Markdown.__exits(file):
            print(f"The file named {file} does not exist")
            return
        
        if not Markdown.isExtensionValid(file):
            print("Invalid file extension")
            return

        fileName = file.replace(".tmd", ".md")
        file_content = Markdown.__getFileContent(file)

        def replace(match)->str:
            balise = match.group(1)
            contenu = match.group(2)

            # TABLE
            if balise == "table":
                return Markdown.__parseTable(contenu)

            format_md = Markdown.__getMarkdownFormat(balise)

            if format_md is None:
                return contenu  

            if balise in ["title", "h1", "h2", "h3", "h4", "h5", "h6"]:
                return f"{format_md} {contenu}\n"

            if balise in ["list", "li"]:
                items = contenu.split("|")
                return "\n".join([f"- {item.strip()}" for item in items]) + "\n"

            if balise == "code":
                return f"```\n{contenu}\n```\n"

            if balise == "link":
                # format attendu: texte | url
                parts = contenu.split("|")
                if len(parts) == 2:
                    return f"[{parts[0].strip()}]({parts[1].strip()})"
                return contenu

            if balise == "img":
                parts = contenu.split("|")
                if len(parts) == 2:
                    return f"![{parts[0].strip()}]({parts[1].strip()})"
                return contenu

            return f"{format_md}{contenu}{format_md}"

        result = re.sub(r"(\w+)\{([^}]*)\}", replace, file_content)

        with open(fileName, "w") as f:
            f.write(result)

        print(f"{file} has been Converted to {fileName} successfully")

    @staticmethod
    def isExtensionValid(file) -> bool:
        return file.endswith(".tmd")

    def __getFileContent(file):
        with open(file, "r") as f:
            return f.read()

    def __exits(file) -> bool:
        return os.path.exists(file)

    def __getMarkdownFormat(balise):
        formats = {
            "title": "#",
            "h1": "#",
            "h2": "##",
            "h3": "###",
            "h4": "####",
            "h5": "#####",
            "h6": "######",

            "italic": "*",
            "i": "*",

            "bold": "**",
            "b": "**",

            "strike": "~~",

            "code": "`",

            "quote": "> ",

            "hr": "---",

            "list": "-",
            "li": "-"
        }
        return formats.get(balise)

    def __parseTable(contenu):
        """
        Format attendu:
        table{
            thead: col1 | col2;
            row: val1 | val2;
            row: val1 | val2
        }
        """

        lignes = [l.strip() for l in contenu.split(";") if l.strip()]

        headers = []
        rows = []

        for ligne in lignes:
            if ligne.startswith("thead:"):
                headers = [h.strip() for h in ligne.replace("thead:", "").split("|")]

            elif ligne.startswith("row:"):
                row = [c.strip() for c in ligne.replace("row:", "").split("|")]
                rows.append(row)

        # sécurité
        if not headers:
            return contenu

        # header
        header_line = "| " + " | ".join(headers) + " |"
        separator = "| " + " | ".join(["---"] * len(headers)) + " |"

        # rows
        rows_lines = []
        for row in rows:
            rows_lines.append("| " + " | ".join(row) + " |")

        return "\n".join([header_line, separator] + rows_lines) + "\n"
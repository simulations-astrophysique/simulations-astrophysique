from xml.etree import ElementTree

from markdown import Extension, Markdown

from zensical.extensions.context import ContextPreprocessor


class CourseSummaryExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        context = ContextPreprocessor.from_markdown(md)
        if context is None:
            raise RuntimeError("The Zensical page context is unavailable.")

        page = context.page
        summary = page.meta.get("summary")
        if not summary or not page.meta.get("contents"):
            return
        if not isinstance(summary, str):
            raise TypeError("The page summary must be a string.")

        wrapper = ElementTree.Element("div")
        paragraph = ElementTree.SubElement(wrapper, "p")
        paragraph.text = summary
        md.treeprocessors["inline"].run(wrapper)
        page.meta["summary_html"] = "".join(
            ElementTree.tostring(element, encoding="unicode", method="html")
            for element in wrapper
        )


def makeExtension(**kwargs: object) -> CourseSummaryExtension:
    return CourseSummaryExtension(**kwargs)

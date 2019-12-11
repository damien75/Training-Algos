from unittest import TestCase

from CareerCup.heading_hierarchy_table import Heading, HierarchyTable


class HierarchyTableTest(TestCase):
    def setUp(self) -> None:
        self.instance = HierarchyTable()

    def test_build_headline_hierarchy_table(self):
        example = [Heading(1, "All About Birds"),
                   Heading(2, "Kinds of Birds"),
                   Heading(3, "The Finch"),
                   Heading(3, "The Swan"),
                   Heading(2, "Habitats"),
                   Heading(3, "Wetlands")]
        self.assertEqual('''Node(Heading(0, ''), List(
	Node(Heading(1, 'All About Birds'), List(
		Node(Heading(2, 'Kinds of Birds'), List(
			Node(Heading(3, 'The Finch'), List())
			Node(Heading(3, 'The Swan'), List())
		))
		Node(Heading(2, 'Habitats'), List(
			Node(Heading(3, 'Wetlands'), List())
		))
	))
))''', str(self.instance.outline(example)))

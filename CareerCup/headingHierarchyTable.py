#source offline Hopper interview question

#input: Ordered list of header elements

#goal: Produce from the list a structured element that can be printed as a Table of Content

#idea: we will use a stack (FIFO) to keep track of our current position in the corresponding
# tree.
# For every element in the list:
# While the new element is shallower or as deep as the last element in the stack, we pop this
# element from the stack and keep looking for the appropriate level
# When we get to the point where the new element is just one level deeper than the last 
# element in the stack then we can add it as a child of this element and to the stack

#Data structure: for each heading we see, we will either add it as a child or go back 
# to look at the other elements already encountered higher in the tree hierarchy
# ==> therefore the good data structure for this problem is a stack

# Printing will just require to go through every child using a DFS

class Heading:
    def __init__(self, weight, text):
        """
        :type weight: int
        :type text: str
        """
        self.__weight = weight
        self.__text = text

    def get_weight(self):
        """
        :rtype: int
        """
        return self.__weight

    def __str__(self):
        """
        :rtype: str
        """
        return 'Heading({}, \'{}\')'.format(self.__weight, self.__text)


class Node:
    def __init__(self, heading, children):
        """
        :type heading: Heading
        :type children: list[Node]
        """
        self.__heading = heading
        self.__children = children

    def add_child(self, child):
        """
        :type child: Node
        """
        self.__children.append(child)

    def get_weight(self):
        """
        :rtype: int
        """
        return self.__heading.get_weight()

    def __str__(self):
        """
        :rtype: str
        """
        s = '\t'*self.get_weight() + 'Node({}, List('.format(self.__heading)
        for child in self.__children:
            s += '\n' + str(child)
        if self.__children:
            s += '\n' + '\t'*self.get_weight() + '))'
        else:
            s += '))'
        return s


def outline(heading_list):
    """
    :type heading_list: list[Heading]
    :rtype: Node
    """
    root = Node(Heading(0, ''), [])
    traversal = [root]
    for heading in heading_list:
        curr_node = traversal.pop()
        while heading.get_weight() <= curr_node.get_weight() and len(traversal) > 0:
            curr_node = traversal.pop()
        assert heading.get_weight() != curr_node.get_weight(), 'We managed to build the following outline: {}' \
            .format(root)
        child = Node(heading, [])
        curr_node.add_child(child)
        traversal.append(curr_node)
        traversal.append(child)
    return root


example = [Heading(1, "All About Birds"),
           Heading(2, "Kinds of Birds"),
           Heading(3, "The Finch"),
           Heading(3, "The Swan"),
           Heading(2, "Habitats"),
           Heading(3, "Wetlands")]
print(outline(example))

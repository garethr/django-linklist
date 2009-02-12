import copy

from linklist.models import Link

def move_up(node):
    "Moves a link up the list, swapping it with the link above."
    try:
        # get the previous link in the list
        # note that this will fail if the link in question is the first link
        prev = Link.objects.filter(link_set=node.link_set, position__lt=node.position).order_by("-position")[0]
        # copy the old position of the link you passed in into a temp variable
        old_position = copy.copy(node.position)
        # then swap the links over
        node.position = prev.position
        prev.position = old_position
        # and save them
        node.save()
        prev.save()
    # if we are the first link in the list then do nothing
    except IndexError:
        pass

def move_down(node):
    "Moves a link down the list, swapping it with the link below."
    try:
        # get the next link in the list
        # note that this will fail if the link in question is the last link
        next = Link.objects.filter(link_set=node.link_set,position__gt=node.position).order_by("position")[0]
        # copy the old position of the link you passed in into a temp variable
        old_position = copy.copy(node.position)
        # then swap the links over
        node.position = next.position
        next.position = old_position
        # and save them
        node.save()
        next.save()
    # if we are the first link in the list then do nothing
    except IndexError:
        pass
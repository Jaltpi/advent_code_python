#!/usr/bin/python3


def square_area_of_box(present_length: int, present_width: int, present_height: int):
    return (
        (2 * present_length * present_width)
        + (2 * present_width * present_height)
        + (2 * present_height * present_length)
    )


def smallest_surface_area(present_length: int, present_width: int):
    return present_length * present_width


presents_to_wrap_dimensions = [(2, 3, 4), (1, 1, 10)]

wrapped_presents_estimate = []

for item in presents_to_wrap_dimensions:
    length, width, height = item
    print(
        f"The current presents dimensions are the following -> length:{length},width:{width},height:{height}"
    )
    required_wrapping_paper = square_area_of_box(length, width, height)
    required_slack = smallest_surface_area(length, width)
    amount_of_wrapping_paper_for_item = required_wrapping_paper + required_slack
    wrapped_presents_estimate.append(amount_of_wrapping_paper_for_item)
    print(
        f"The current presents dimensions required_wrapping_paper:{required_wrapping_paper} needs to have the additional slack of:{required_slack}, we expect the amount_of_wrapping_paper_for_item to require square feet of:{amount_of_wrapping_paper_for_item}"
    )

total_wrapping_paper = sum(wrapped_presents_estimate)
print(f"The total required wrapping paper for elves to order: {total_wrapping_paper}")

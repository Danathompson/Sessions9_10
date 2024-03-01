def is_valid_url(url):
    # Check if the URL starts with http:// or https:// using if and direct comparison
    if url.startswith("http://") or url.startswith("https://"):
        valid_start = True
    else:
        valid_start = False

    # Proceed only if the start is valid
    if valid_start:
        # Initialize variables for further checks
        scheme_end = url.find("://") + 3  # Find where the scheme ends
        domain_start = scheme_end
        dot_position = url.find(".", domain_start)
        space_position = url.find(" ", domain_start)

        # Ensure there's a dot in the domain part, and check spacing
        if dot_position > -1:
            has_dot = True
        else:
            has_dot = False

        # Check if there's a space in the URL after the scheme
        if space_position == -1:
            no_space = True
        else:
            no_space = False

        # Ensure dot exists and there are no spaces for it to be a valid URL
        if has_dot and no_space:
            return True
        else:
            return False
    else:
        return False


# Example usage
print(is_valid_url("http://google.com"))  # Expected to return True
print(is_valid_url("https://example site.com"))  # Expected to return False

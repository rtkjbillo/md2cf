class FakePage(object):
    """Assert helper that always matches."""

    def __init__(self, **kwargs):
        self.attrs_to_compare = dict()
        for parameter in [
            "title",
            "body",
            "attachments",
            "file_path",
            "page_id",
            "parent_id",
            "parent_title",
            "space",
        ]:
            param_value = kwargs.get(parameter, None)
            if param_value:
                self.attrs_to_compare[parameter] = param_value

    def __eq__(self, actual):
        for attribute_name, attribute_value in self.attrs_to_compare.items():
            actual_attribute = getattr(actual, attribute_name, None)
            if actual_attribute != attribute_value:
                # print(f"{attribute_name}={repr(attribute_value)} != {repr(actual_attribute)}")
                return False
        return True

    def __repr__(self):
        return "FakePage({})".format(
            ", ".join(
                [
                    "{}={}".format(name, repr(value))
                    for name, value in self.attrs_to_compare.items()
                ]
            )
        )

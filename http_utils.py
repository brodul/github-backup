def parse_link_header(value):
    def parse_link(value):
        url_value, relation_value = value.split('; ')

        assert url_value[0] == '<'
        assert url_value[-1] == '>'
        url = url_value[1:-1]

        assert relation_value.startswith('rel="')
        assert relation_value.endswith('"')
        relation = relation_value[5:-1]

        return (relation, url)

    return dict(map(parse_link, value.split(', ')))

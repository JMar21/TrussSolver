import re
from structures.model.bar import StrBar
__BAR_REGEX = r'(?P<id>\d+)\s*:\s*' \
            r'\((?P<start_id>\d+)\s*->\s*(?P<end_id>\d+)\)\s*' \
            r'(?P<sec>[\d\.]+)\s+' \
            r'(?P<young>[\d\.]+)'

def parse_bar(bar_str, nodes_dict):
    match = re.match(__BAR_REGEX, bar_str)
    if not match:
        raise ValueError(f'Cannot parse {bar_str}')
    _id = int(match.group('id'))
    start_id = int(match.group('start_id'))
    end_id = int(match.group('end_id'))
    section=  float(match.group('sec'))
    young = float(match.group('young'))
    start_node = nodes_dict[start_id]
    if start_node is None:
        raise ValueError('undefined start node')
    end_node = nodes_dict[end_id]
    if end_node is None:
        raise ValueError('undefined end node')
    return StrBar(_id, start_node, end_node, section, young)
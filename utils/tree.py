
def treeFilter(serializer_data, filter_name=None):
    """
    树型化
    """
    tree_dict = {}
    tree_data = []
    try:
        for item in serializer_data:
            tree_dict[item['id']] = item
        for i in tree_dict:
            if filter_name:
                if i not in filter_name:
                    continue
            if tree_dict[i]['pid']:
                pid = tree_dict[i]['pid']
                parent = tree_dict[pid]
                parent.setdefault('children', []).append(tree_dict[i])
            else:
                tree_data.append(tree_dict[i])
        results = tree_data
    except KeyError:
        results = serializer_data
    return results

def extract_metadata(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        node_list = list(tree.nodes.values())
        metadata = []
        
        for node in node_list:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                name = getattr(node, 'name', None)
                params = getattr(node, 'params', None)
                body = [ast.copy_location(n) for n in getattr(node, 'body', [])]
                
                for i, line in enumerate(body):
                    node_line = ast.copy_location(ast.parse(str(line))[0], 
line.lstrip())
                    setattr(node_line, 'lineno', node.lineno + i + 1)
                    setattr(node_line, 'original_lineno', node.lineno + i + 1)
                    metadata.append({
                        'name': name,
                        'params': params,
                        'body_lines': [node_line] if isinstance(node_line, ast.Node)
                    })
        
        return metadata
    except Exception as e:
        print(f"Error extracting {filename}: {e}")
        return None


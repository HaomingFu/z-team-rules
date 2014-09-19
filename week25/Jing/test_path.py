def simplifyPath(path):
    pathEle = path.split("/")
    stack = []
    for ele in pathEle:
        if ele == "..":
            if stack:
                stack.pop()
        elif ele and ele != ".":
            stack.append(ele)
    if not stack:
        return "/"
    else:
        return "/"+"/".join(stack)

print(simplifyPath("/../"))
print(simplifyPath("/a/./b/../../c/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/"))

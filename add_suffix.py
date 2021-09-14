def add_suffix(file: str, suffix: str):
    assert len(file.rsplit(".", 1)) == 2, "file should have an extension!"
    base, extension = file.rsplit(".", 1)
    res_file = base+suffix + "." + extension
    return res_file


if __name__ == "__main__":
    file = r"./xxx.jpg"
    print("original file: {}".format(file))
    file = add_suffix(file, r"_result")
    print("new file: {}".format(file))

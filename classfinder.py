def get_filename():
    filename = input("Whats the file name my dear user? ");
    return filename;

def open_file(filename):
    classes = [];
    try:
        f = open(filename, "r", encoding = "utf=8");
    except FileNotFoundError:
        print('Invalid file! try again');
        main();

    else:     #continue if file not found
        for x in f:
            classes.append(x);
        f.close();
        return classes;


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        common = (a_set & b_set);
        print("The common elements are: ");
        for y in common:
            y.strip('\n');
            print(y);
    else:
        print("No common classes :( Sorry user!");

def main():
    print("Enter file name for list A")
    list_a = open_file(get_filename());
    print("Enter file name for list B")
    list_b = open_file(get_filename());
    common_member(list_a, list_b);

if __name__ == "__main__":
    main();

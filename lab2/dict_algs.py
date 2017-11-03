def staff (emps, age1=18):
    for emp in emps:
        for chd in emp["children"]:
            if chd["age"] > age1:
                print (emp['name'])
                break

if __name__ == '__main__':
    ivan = {
        "name": "ivan",
        "age": 34,
        "children": [{
            "name": "vasja",
            "age": 12,
        }, {
            "name": "petja",
            "age": 10,
        }],
    }

    darja = {
        "name": "darja",
        "age": 41,
        "children": [{
            "name": "kirill",
            "age": 21,
        }, {
           "name": "pavel",
           "age": 15,
        }],
    }

    emps = [ivan, darja]
    staff (emps)
    # print(ivan)
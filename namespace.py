


def scopeTest():
    def do_local():
        var="This is local"

    def do_nonlocal():
        nonlocal var;
        var= "This is non local"

    def do_global():
        global var
        var= "This is Global"

    var ="test";
    do_local();
    print("After local assignment",var);
    do_nonlocal()
    print("After non local assignment", var);
    do_global()
    print("After global assignment",var);


scopeTest()
print("in global scope", var);
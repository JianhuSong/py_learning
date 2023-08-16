#include <iostream>
#include <string>

class Name
{
    public:
    Name(const std::string &name, int a):_name(name), _a(a) {}
    Name() 
    {
        _name = "asdasdasd"; //静态成员只能在初始化列表中初始化
        _a    = 100;
    }
    ~Name() = default;
    private:
        const std::string _name;
        int _a;
};

int main(int argc, const char** argv) {
    Name name = Name("sdasfasdf", 123);
    return 0;
}
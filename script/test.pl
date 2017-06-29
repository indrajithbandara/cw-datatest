#!usr/bin/perl
@hits = (25, 30, 40);             
@names = ("google", "runoob", "taobao");

print "\$hits[0] = $hits[0]\n";
print "\$hits[1] = $hits[1]\n";
print "\$hits[2] = $hits[2]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";

# 创建一个简单是数组
@sites = ("google","runoob","taobao");
print "1. \@sites  = @sites\n";

# 在数组结尾添加一个元素
push(@sites, "baidu");
print "2. \@sites  = @sites\n";

# 在数组开头添加一个元素
unshift(@sites, "weibo");
print "3. \@sites  = @sites\n";

# 删除数组末尾的元素
pop(@sites);
print "4. \@sites  = @sites\n";

# 移除数组开头的元素
shift(@sites);
print "5. \@sites  = @sites\n";
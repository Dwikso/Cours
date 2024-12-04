var fac = function(n) {
    if (n === 0) {
        return 1;
    }
    return n * fac(n - 1);
}

var memoFac = (function() {
    var cache = {};

    return function (x) {
        if(!(x in cache)) {
            console.log('mise en cache de fac(' + x + ')');
            cache[x] = fac(x);
        }
        return cache[x];
    }
}());


var memoFac2 = (function() {
    var cache = {};
    return function f(x) {
        var value
        if(!(x in cache)) {
            console.log('mise en cache de fac(' + x + ')');
            if (x === 0) {
                value = 0;
            } else if (x === 1) {
                value = 1;
            } else {
                value = f(x - 1) + f(x - 2);
            }
            cache[x] = value;
        }
        return cache[x];
    }
}());

function fibbonnaci(n) {
    if (n === 0 || n === 1) {
        return n;
    } else  {
        return fibbonnaci(n - 1) + fibbonnaci(n - 2)
    }
}

var memoFibo = (function() {
    var cache = {};
    return function f(x) {
        var value;
        if(!(x in cache)) {
            console.log('mise en cache de fac(' + x + ')');
            if (x === 0) {
                value = 1;
            } else {
                value = f(x - 1) + f(n - 2)
            }
            cache[x] = value;
        }
        return cache[x];
    }
}());


var memoSuiteGeo = (function () {
    var cache = {};
    return function f(first, r, n) {
        var value;
        cache[first] = cache[first] || [];
        cache[first][n] = cache[first][n] || {};
        if (first in cache && r in cache[first] && n in cache[first][r]) {
            value = cache[first][r][n];
        } else {
            if (n == 1)
                value = first
            else
                value = r * f(first,r,n - 1);
            cache[first][r][n] = value
        }
        return value
    }
    return f
}())



console.log(memoFac2(10))
console.log(memoFac2(20))
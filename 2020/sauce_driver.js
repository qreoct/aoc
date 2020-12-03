// take input, wrap in backticks
// run `xxxxx input xxxxxx`.split("\n") in console
// right click > store as global variable (it should be named temp1)
// run copy(JSON.stringify(temp1))
// the array is now stored on clipboard

let input = ["0"];

function array_to_int(A){
    for(let i = 0; i < array_length(A); i = i + 1){
            A[i] = parse_int(A[i], 10);
    }
}

array_to_int(input);

function day1_silv(param){
    return 0;
}

function day1_gold(param){
    return 0;
}

const t1 = get_time();
const silv = day1_silv(input);
const t2 = get_time();
const t3 = get_time();
const gold = day1_gold(input);
const t4 = get_time();
display("SILV: " + stringify(silv) + " in " + stringify(t2-t1) + "ms");
display("GOLD: " + stringify(gold) + " in " + stringify(t4-t3) + "ms");

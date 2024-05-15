def calculateTax(sum, proc, purpose):
    FinSum = sum * proc/100
    return [FinSum, sum, proc, purpose]
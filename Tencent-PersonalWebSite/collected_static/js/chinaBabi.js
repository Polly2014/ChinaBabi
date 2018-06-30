"use strict";

var BabiInfo = function(text){
	if (text) {
		var obj = JSON.parse(text);
		this.companyAdress = obj.companyAdress;
		this.detailInfo = obj.detailInfo;
	} else {
		this.companyAdress = "";
		this.detailInfo = "";
	}
}

BabiInfo.prototype = {
	toString: function () {
		return JSON.stringify(this);
	}
};

var ChinaBabiContract = function(){
	LocalContractStorage.defineMapProperty(this, "data", {
		parse: function (text) {
			return new BabiInfo(text);
		},
		stringify: function (o) {
			return o.toString();
		}
	});
};

ChinaBabiContract.prototype = {
	init: function () {
		// todo
	},
	save: function(babiID, babiDetailInfo){
		babiID = babiID.trim();
		babiDetailInfo = babiDetailInfo?babiDetailInfo.trim():"";
		if (babiID === "" || babiID.length!=36){
			throw new Error("Wrong BabiID Format");
		}

		var from = Blockchain.transaction.from;
		var babiInfo = this.data.get(babiID);
		if (babiInfo){
			throw new Error("BabiInfo has been occupied");
		}
		console.log(from+'|'+babiInfo);
		babiInfo = new BabiInfo();
		babiInfo.companyAdress = from;
		babiInfo.detailInfo = babiDetailInfo;

		this.data.put(babiID, babiInfo);
	},
	get: function(babiID){
		babiID = babiID.trim();
		if ( babiID === "" ) {
			throw new Error("Empty BabiID")
		}
		return this.data.get(babiID);
	}
}

module.exports = ChinaBabiContract;

// n1ivkWsrdK2u2DAMGtyyyHEQ6R8Ev37ioPR


// Adress: n1oRcaG7KLV9d9ohDBGHst5ZgbFRmspPed9
// Hash: 6e6ed2d12953d899ffa3864db9127d0ff4dd68b96c0f2433e9150ddab90276ae
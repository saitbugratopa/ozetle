chrome.tabs.getSelected(null,function(tab) {

    let myurl = tab.url;

    if(myurl.includes("haber7.com")){
        var newURL = "http://localhost:5000/ozetle?url="+myurl;
        chrome.tabs.create({ url: newURL });
    }else{
        alert('Bu Eklenti Sadece Haber7.com da calisir.')
    }
});

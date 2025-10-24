let obs = {
    firms_urls: [],
    next_btn: null,
    getFirms: async function () {
        let co = this.firms_urls.length;
        let last = null;
        document.querySelectorAll('a').forEach((node) => {
            let h = node.getAttribute('href');
            if (h && h.indexOf('/firm/') !== -1) {
                this.firms_urls.push(h.split('?')[0]);
                last = node;
            }
        });
        this.firms_urls = Array.from(new Set(this.firms_urls));
        console.log(this.firms_urls.length,co);
        if(co == this.firms_urls.length){
            this.print();
            return;
        }
        if(!this.next_btn){
            this.getNextBtn(last);
        }
        this.next_btn.click();

        setTimeout(() => {
            this.getFirms();
        },3000);
    },
    getNextBtn: function (last) {
        console.log(last);
        let p = last.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.childNodes;
        this.next_btn = p[p.length - 2].childNodes[1].childNodes[1];
    },
    print: function (){
        let str = JSON.stringify(this.firms_urls);
        let div = document.createElement("div");
        div.classList.add('result_json');
        div.textContent = str;
        document.querySelector('body').innerHTML = "";
        document.querySelector('body').appendChild(div);

    }
};

obs.getFirms();

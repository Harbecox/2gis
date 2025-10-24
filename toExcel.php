<?php

use Symfony\Component\DomCrawler\Crawler;

require './vendor/autoload.php';

$dir = "htmls/";
$headers = ['name','type','city','address','site','phone'];
$csv[] = "\xEF\xBB\xBF".implode(";",$headers);
foreach (scandir($dir) as $k => $file) {
    if($k == 200){
        break;
    }
    if(is_file($dir.$file)){
        $e = explode(".", $file);
        $id = $e[0];
        echo $id."\n";
        $html = file_get_contents($dir.$file);
        $start = strpos($html,"var initialState = JSON.parse('");
        $start = strpos($html,"{",$start);
        $end = strpos($html,"')",$start);
        $json_str = substr($html,$start,$end-$start);
        $json_str = str_replace('\\\\', '\\', $json_str);
        $json = json_decode($json_str,true);
        $data = $json['data']['entity']['profile'][$id]['data'];
        $item['name'] = $data['name_ex']['primary'];
        $item['type'] = $data['name_ex']['extension'] ?? "";
        $d = [];
        foreach ($data['adm_div'] as $i){
            $d[] = $i['name'];
        }
        $item['city'] = implode(", ",$d);
        $item['address'] = $data['address_name'] ?? "";
        $item['site'] = "";
        $p = [];
        if(isset($data['contact_groups'])){
            foreach ($data['contact_groups']  as $i){
                if(isset($i['contacts'])){
                    foreach ($i['contacts'] as $j){
                        if($j['type'] == 'phone'){
                            $p[] = $j['value'];
                        }elseif($j['type'] == 'website'){
                            $item['site'] = $j['url'];
                        }
                    }
                }

            }
        }
        $item['phone'] = implode(", ",$p);

        foreach ($item as &$a){
            $a = str_replace(";",",",$a);
        }
        $csv[] = implode(';',$item);
    }
    file_put_contents("data.csv",implode("\n",$csv));
}
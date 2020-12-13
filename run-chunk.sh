cd create-chunk
sudo python sel.py
sudo python get_text.py
sudo python topic_model.py
sudo python get_idata.py
sudo python img-dm.py
sudo python img-param.py
sudo python thumbnail.py
sudo cp param/img-param.lisp /actr6/distr-model/param/
sudo cp dm/img-dm.lisp /actr6/distr-model/param/
sudo cp -r visicon/idata /actr6/distr-model/param/
cd /

pull:
	mkdir -p /tmp/ehub_data
	aws s3 cp s3://net.energyhub.assets/public/dev-exercises/audit-data.tar.gz /tmp/ehub_data
	tar xvzf /tmp/ehub_data/audit-data.tar.gz
	rm -rf rm -rf /tmp/ehub_data

clean:
	rm -rf 2016

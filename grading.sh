#alias gcc="gcc -w"
filelist=`find -f notfinished`
root="/Users/tianlong/Desktop/ray_tracing_grading"
for filename in $filelist
do
	if [[ $filename == *.zip ]]
	then
  		#echo $filename
  		len=`expr length $filename` 
  		len=$(($len-4))
  		path_no_dot=${filename:0:len}
  		path="./$path_no_dot"
  		#echo $path
  		unzip -q $filename -d $path
  		makefiles=`find $path -name "CMakeLists.txt"`
  		#echo $makefiles
  		for makefile in $makefiles
		do
			echo $makefile
			makedir=`dirname $makefile`
			cd $makedir
			cmake . 1>/dev/null
			make 1>/dev/null
			mkdir result
			cd scenes
			###
			../bin/mk/01_raytrace 01_sphere.json
			../bin/mk/01_raytrace 02_quad.json
			../bin/mk/01_raytrace 03_plane.json
			../bin/mk/01_raytrace 04_balls.json
			../bin/mk/01_raytrace 05_refl.json
			../bin/mk/01_raytrace 06_aa.json
			###
			cd ..
			###
			png_diff diff scenes/01_sphere_ref.png scenes/01_sphere.png result/001_diff.png
			png_diff diff scenes/02_quad_ref.png scenes/02_quad.png result/002_diff.png
			png_diff diff scenes/03_plane_ref.png scenes/03_plane.png result/003_diff.png
			png_diff diff scenes/04_balls_ref.png scenes/04_balls.png result/004_diff.png
			png_diff diff scenes/05_refl_ref.png scenes/05_refl.png result/005_diff.png
			png_diff diff scenes/06_aa_ref.png scenes/06_aa.png result/006_diff.png
			###

			resultsforcheck="$root/$path_no_dot"
			cp -r result $resultsforcheck

			cd $root
			break
		done
  		#echo ${makefiles[$((1))]}
  		#rm -fr $path
	fi	
done
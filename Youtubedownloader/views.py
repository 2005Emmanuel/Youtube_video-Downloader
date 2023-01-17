from django.shortcuts import render, redirect, HttpResponse
# from django.views.decorators.csrf import csrf_protect
from django.views.generic import View 
from pytube import YouTube
import os
from wsgiref.util import FileWrapper

#build your view here
def ytd(request):
	return render(request, 'index.html') #view to get the hompage

def download_page(request): #view to get the resolution and url of the page
	global url
	url = request.GET.get('url')

	yt = YouTube(url)
	global streams
	streams = yt.streams

	res = []
	ores = []
	for i in streams:
		onlyres = i.resolution

		string = str(i.resolution) + ' ' + str(i.filesize_approx // 1048576) + 'mb'

		res.append(string)
		ores.append(onlyres)
	
	ores = list(dict.fromkeys(ores))

	try:
		for j in range(len(ores)):
			if ores[j] == None:
				ores.pop(j)

	except:
		pass
    
    
	for k in range(len(ores)):
		ores[k] = ores[k] + ' ' + str(streams.filter(res=ores[k]).first().filesize // 1048576) + 'mb'
  
	
	title = yt.title
	author = yt.author
	length = str(yt.length//100) + ' minutes'
	if length == 0:
		length = str(yt.length) + ' seconds'

	thumbnail = yt.thumbnail_url
	print(thumbnail)


	res = list(dict.fromkeys(res))

	return render(request, 'download.html', {
		'onlyres': ores,
		'res': res,
		'title': title,
		'author': author,
		'length': length,
		'thumbnail': thumbnail,
	})

def success(request, res): #view to download the video it is done with file handling
	global url

	homedir = os.path.expanduser("~")

	dirs = homedir + '/Downloads/'
  
	yt = YouTube(url)
	title = yt.title
	print(title)
	res,b = res.split()
	size = streams.filter(res=res).first().filesize // 1048576
	print(size)
	if request.method == 'POST' and size < 900:
		streams.filter(res=res).first().download(output_path = dirs, filename = "video.mp4")
		file = FileWrapper(open(f'{dirs}/video.mp4', 'rb'))
		# path =  '/home/runner/youtube-video-downloader/downloads/video' + '.mp4'
		# o = dirs + title + '.mp4'
		response = HttpResponse(file, content_type = 'vnd.mp4') #vnd.mp4
		response['Content-Disposition'] = 'attachment; filename = "video.mp4"'
		# os.remove(f'{dirs}/video.mp4')
		return response
	else:
		return render(request, 'error.html')
        
        
    # def post(self,request):
    #     # for fetching the video
    #     if request.POST.get('fetch-vid'):
    #         self.url = request.POST.get('given_url')
    #         video = YouTube(self.url)
    #         vidTitle,vidThumbnail = video.title,video.thumbnail_url
    #         qual,stream = [],[]
    #         for vid in video.streams.filter(progressive=True):
    #             qual.append(vid.resolution)
    #             stream.append(vid)
    #         context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
    #                     'qual':qual,'stream':stream,
    #                     'url':self.url}
    #         return render(request,'index.html',context)

    #     # for downloading the video
    #     elif request.POST.get('download-vid'):
    #         homedir = os.path.expanduser("~")

	#         dirs = homedir + '/Downloads/
    #         streams.filter(res=res).first().download(output_path = dirs, filename = "video.mp4")
    #         file = FileWrapper(open(f'{dirs}/video.mp4', 'rb'))
    #         # path =  '/home/runner/youtube-video-downloader/downloads/video' + '.mp4'
    #         # o = dirs + title + '.mp4'
    #         response = HttpResponse(file, content_type = 'application/vnd.mp4')
    #         response['Content-Disposition'] = 'attachment; filename = "video.mp4"'
    #         os.remove(f'{dirs}/video.mp4')
    #         return response
        #     self.url = request.POST.get('given_url')
        #     video = YouTube(self.url)
        #     stream = [x for x in video.streams.filter(progressive=True)]
        #     video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
            
        #     video_qual.download(output_path= dir, filename="video.mp4") 
        #     file = FileWrapper(open(f'{dir}/video.mp4', 'rb'))
		# # path =  '/home/runner/youtube-video-downloader/downloads/video' + '.mp4'
		# # o = dirs + title + '.mp4'
        #     response = HttpResponse(file, content_type = 'application/vnd.mp4')
        #     response['Content-Disposition'] = 'attachment; filename = "video.mp4"'
        #     os.remove(f'{dir}/video.mp4')
        #     return response
            
        # return redirect('home')
    # response = HttpResponse(video, content_type='video/mp4')
    #         response['Content-Disposition'] = 'attachment; filename="video.mp4"'
# return render(request,'index.html')
    # from pytube import YouTube

# def download_video(request):
#     video_url = request.GET.get('video_url')
#     yt = YouTube(video_url)
#     video = yt.get('mp4', '720p')
#     response = HttpResponse(video.streams.first().download(), content_type='video/mp4')
#     response['Content-Disposition'] = 'attachment; filename="video.mp4"'
#     return response
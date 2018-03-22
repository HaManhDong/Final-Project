import cv2

destination_file = 'video.avi'
fps = 10.0
size = (640, 480)

codecs = [
    '4XMV',
    'AASC',
    'AP41',
    'ASV1',
    'ASV2',
    'AVC1',
    'AVRN',
    'AYUV',
    'BLZ0',
    'COL0',
    'COL1',
    'CRAM',
    'CSCD',
    'CVID',
    'CYUV',
    'DIV1',
    'DIV2',
    'DIV3',
    'DIV4',
    'DIV5',
    'DIV6',
    'DIVX',
    'DUCK',
    'DV25',
    'DVHD',
    'DVR ',
    'DVSD',
    'DVSL',
    'DX50',
    'FFV1',
    'FFVH',
    'FLV1',
    'FMP4',
    'FPS1',
    'FSV1',
    'H261',
    'H263',
    'H264',
    'HDYC',
    'HFYU',
    'I263',
    'I420',
    'IJPG',
    'IV31',
    'IV32',
    'IYUV',
    'JPEG',
    'JPGL',
    'KMVC',
    'LJPG',
    'LOCO',
    'M4S2',
    'MJ2C',
    'MJLS',
    'MJPG',
    'MMES',
    'MP42',
    'MP43',
    'MP4S',
    'MP4V',
    'MPEG',
    'MPG1',
    'MPG2',
    'MPG3',
    'MPG4',
    'MRLE',
    'MSVC',
    'MSZH',
    'PIM1',
    'Q1.0',
    'Q1.1',
    'QPEG',
    'RMP4',
    'RT21',
    'SEDG',
    'SNOW',
    'SVQ1',
    'TGA ',
    'THEO',
    'TM20',
    'TSCC',
    'U263',
    'ULTI',
    'UMP4',
    'UYVY',
    'VCR1',
    'VCR2',
    'VIV1',
    'VIXL',
    'VMNC',
    'VP30',
    'VP31',
    'VP50',
    'VP60',
    'VP61',
    'VP62',
    'VP6F',
    'VSSH',
    'WHAM',
    'WMV1',
    'WMV2',
    'WMV3',
    'WMVA',
    'WNV1',
    'WV1F',
    'WVC1',
    'X264',
    'XVID',
    'XXAN',
    'Y422',
    'Y800',
    'YUV1',
    'YUY2',
    'YV12',
    'ZLIB',
    'ZMBV'
]

for codec in codecs:
    codec_int = cv2.cv.CV_FOURCC(codec[0], codec[1], codec[2], codec[3])
    # print('\nAttempting to create VideoWriter for "' + codec + '".')
    try:
        writer = cv2.VideoWriter(destination_file, codec_int, fps, size, True)

        if writer.isOpened():
            print(codec)
    except:
        pass
    # else:
    #     print('Failed.')
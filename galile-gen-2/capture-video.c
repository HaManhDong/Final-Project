static void open_device(void) {
	fd = open(dev_name, O_RDWR /* reuired */ | O_NONBLOCK, o);
	if(-1 == fd) {
		fprintf(stderr, "Cannot open '%s': %d, %s\n", dev_name, errno, strerror(errno));
		exit(EXIT_FAILURE);
	}

}

struct v4l2_capability cap;

if (-1 == xioctl(fd, VIDIOC_QUERYCAP, &cap)) {
	if (EINVAL == errno) {
		fprintf(stderr, "%s is no V4L2 device\n", dev_name);
		exit(EXIT_FAILURE);
	} else {
		errno_exit("VIDIOC_QUERYCAP");
	}
}

struct v4l2_crop crop;
struct v4l2_cropcap cropcap;

cropcap.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

if (0 == xioctl(fd, VIDIOC_CROPCAP, &cropcap)) {
	crop.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
	crop.c = cropcap.defrect; /* reset to default */
	
	if (-1 == xioctl(fd, VIDIOC_S_CROP, &crop)) {
		switch (errno) {
		case EINVAL:
			/* Cropping not supported. */
			break;
		default:
			/* Errors ignored. */
			break;
		}
	}
}

fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
	if (force_format) {
		fmt.fmt.pix.width = 1280;
		fmt.fmt.pix.height = 720;
		fmt.fmt.pix.pixelformat = V4L2_PIX_FMT_MJPEG;
		fmt.fmt.pix.field = V4L2_FIELD_NONE;


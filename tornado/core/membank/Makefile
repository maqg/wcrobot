all::
	${TOPDIR}/tornado/octpyc

clean::
	rm -rf *.pyc

install::
	${MKDIR} -p $(TOPDIR)/OCTFrame/core/membank
	${COPY} *.pyc $(TOPDIR)/OCTFrame/core/membank/.
	${COPY} dbrobot $(TOPDIR)/OCTFrame/core/membank/.

real_install::
	${MKDIR} -p $(DSTDIR)/OCTFrame/core/membank/.
	${COPY} *.pyc $(DSTDIR)/OCTFrame/core/membank/.
	${COPY} dbrobot $(DSTDIR)/OCTFrame/core/membank/.
